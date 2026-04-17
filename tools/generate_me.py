#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from pathlib import Path


FIRST_PERSON = {"我", "自己", "本人"}
STYLE_KEYWORDS = ["说话", "表达", "语气", "风格", "直接", "简洁", "具体", "节奏", "清楚"]
PREFERENCE_KEYWORDS = ["喜欢", "不喜欢", "偏好", "习惯", "倾向", "一般会", "通常会"]
BOUNDARY_KEYWORDS = ["不会", "不要", "不能", "边界", "原则", "禁区", "不想", "别", "而不是"]
ANTI_PATTERN_KEYWORDS = ["不像我", "不太像我", "我不会这样说", "别写成", "不要写成"]
DECISION_KEYWORDS = ["先做", "再", "决定", "判断", "倾向", "优先", "再决定", "先把"]
EMOTION_KEYWORDS = ["情绪", "态度", "温和", "克制", "冷静", "热情", "外放"]
VALUE_KEYWORDS = ["真实", "准确", "具体", "讲清楚", "事实", "原则", "边界"]
FACT_MARKERS = ["我是", "我在", "我做", "我有", "我来自", "我负责", "我一直", "我曾经"]
STYLE_HINT_PREFIXES = ["更像我的表达", "我说话", "我表达", "我希望别人觉得我"]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff_-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "me"


def load_records(paths: list[Path]) -> list[dict]:
    records = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            records.extend(data)
    return records


def unique_keep_order(items: list[str], limit: int) -> list[str]:
    result = []
    seen = set()
    for item in items:
        normalized = item.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
        if len(result) >= limit:
            break
    return result


def contains_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def is_first_person(text: str) -> bool:
    return any(marker in text for marker in FIRST_PERSON)


def is_fact_like(text: str) -> bool:
    if contains_any(text, STYLE_KEYWORDS + PREFERENCE_KEYWORDS + BOUNDARY_KEYWORDS + ANTI_PATTERN_KEYWORDS + VALUE_KEYWORDS):
        return False
    return any(marker in text for marker in FACT_MARKERS)


def is_style_like(text: str) -> bool:
    return contains_any(text, STYLE_KEYWORDS) or any(text.startswith(prefix) for prefix in STYLE_HINT_PREFIXES)


def is_boundary_like(text: str) -> bool:
    return contains_any(text, BOUNDARY_KEYWORDS) or "不喜欢" in text


def is_value_like(text: str) -> bool:
    if any(fragment in text for fragment in ["希望别人觉得", "讲清楚", "事实", "真实", "准确", "具体"]):
        return True
    return contains_any(text, VALUE_KEYWORDS)


def normalize_preference(text: str) -> str:
    if "不喜欢太夸张" in text or ("不喜欢" in text and "夸张" in text):
        return "不喜欢太夸张的表达"
    if "简洁" in text and "具体" in text:
        return "偏好简洁具体的表达"
    if "一般会先做一个最小可用版本" in text:
        return "偏好先做最小可用版本再迭代"
    return text


def summarize_style(text: str) -> str:
    if "简洁" in text and "具体" in text:
        return "表达偏简洁具体"
    if "直接" in text and "咄咄逼人" in text:
        return "说话直接，但不过分有压迫感"
    if "直接" in text:
        return "说话偏直接"
    if "清楚" in text:
        return "表达时更重视讲清楚"
    if text.startswith("更像我的表达是："):
        return text.replace("更像我的表达是：", "").strip()
    return text


def summarize_decision(text: str) -> str:
    if "先做一个最小可用版本" in text:
        return "倾向先做最小可用版本，再逐步完善"
    if "先把事情讲清楚，再决定做不做" in text:
        return "倾向先澄清问题，再决定是否执行"
    return text


def summarize_emotion(text: str) -> str:
    if "不是咄咄逼人" in text:
        return "表达直接，但会控制压迫感"
    if "情绪很满" in text:
        return "不喜欢情绪过满的表达状态"
    if "外放" in text:
        return "不采用过度外放的情绪表达"
    if "克制" in text:
        return "情绪表达偏克制"
    return text


def summarize_value(text: str) -> str:
    if "越具体越好" in text:
        return "重视具体、清晰的表达"
    if "讲清楚" in text:
        return "重视先把事情讲清楚"
    if "希望别人觉得我表达清楚" in text:
        return "希望给人表达清楚、不过度情绪化的印象"
    return text


def classify_records(records: list[dict]) -> dict:
    buckets = {
        "facts": [],
        "preferences": [],
        "style_signals": [],
        "boundaries": [],
        "values": [],
        "anti_patterns": [],
        "quotes": [],
        "decision_signals": [],
        "emotion_signals": [],
    }

    for record in records:
        text = str(record.get("text", "")).strip()
        speaker = str(record.get("speaker", "unknown")).strip()
        kind = str(record.get("kind", "")).strip()
        if not text:
            continue

        buckets["quotes"].append(text)

        anti = kind == "correction" or contains_any(text, ANTI_PATTERN_KEYWORDS)
        boundary = is_boundary_like(text)
        style = is_style_like(text)
        preference = contains_any(text, PREFERENCE_KEYWORDS)
        decision = contains_any(text, DECISION_KEYWORDS)
        emotion = contains_any(text, EMOTION_KEYWORDS)
        value = is_value_like(text)
        fact = is_first_person(text) and is_fact_like(text)

        if anti:
            buckets["anti_patterns"].append(text)
            continue

        if preference:
            buckets["preferences"].append(normalize_preference(text))

        if boundary:
            buckets["boundaries"].append(text)

        if value:
            buckets["values"].append(summarize_value(text))

        if style:
            buckets["style_signals"].append(summarize_style(text))

        if decision:
            buckets["decision_signals"].append(summarize_decision(text))

        if emotion:
            buckets["emotion_signals"].append(summarize_emotion(text))
        elif speaker not in {"我", "自己", "本人"} and style:
            buckets["emotion_signals"].append(summarize_emotion(text))

        if fact:
            buckets["facts"].append(text)

    for key, limit in {
        "facts": 12,
        "preferences": 10,
        "style_signals": 10,
        "boundaries": 8,
        "values": 8,
        "anti_patterns": 8,
        "quotes": 8,
        "decision_signals": 6,
        "emotion_signals": 6,
    }.items():
        buckets[key] = unique_keep_order(buckets[key], limit)

    return buckets


def collect_stats(records: list[dict]) -> dict:
    sources = Counter(str(item.get("source", "unknown")) for item in records)
    speakers = Counter(str(item.get("speaker", "unknown")) for item in records)
    return {
        "record_count": len(records),
        "source_count": len(sources),
        "sources": dict(sources),
        "speakers": dict(speakers),
    }


def build_self(name: str, buckets: dict) -> str:
    lines = [
        "# Self",
        "",
        "## 基本信息",
        f"- 代号：{name}",
        "",
        "## 明确事实",
    ]
    lines.extend([f"- {item}" for item in buckets["facts"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 稳定偏好",
    ])
    lines.extend([f"- {item}" for item in buckets["preferences"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 价值观",
    ])
    lines.extend([f"- {item}" for item in buckets["values"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 边界",
    ])
    lines.extend([f"- {item}" for item in buckets["boundaries"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 待确认",
        "- 需要继续补充长期稳定的背景信息与重要关系",
    ])
    return "\n".join(lines) + "\n"


def build_persona(buckets: dict) -> str:
    lines = [
        "# Persona",
        "",
        "## 说话节奏",
    ]
    lines.extend([f"- {item}" for item in buckets["style_signals"][:4]] or ["- 暂无"])
    lines.extend([
        "",
        "## 常见表达风格",
    ])
    lines.extend([f"- {item}" for item in buckets["style_signals"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 情绪与态度",
    ])
    lines.extend([f"- {item}" for item in buckets["emotion_signals"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 决策倾向",
    ])
    lines.extend([f"- {item}" for item in buckets["decision_signals"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 明显不像他的表达",
    ])
    lines.extend([f"- {item}" for item in buckets["anti_patterns"]] or ["- 暂无"])
    lines.extend([
        "",
        "## 代表性原句",
    ])
    lines.extend([f"- {item}" for item in buckets["quotes"]] or ["- 暂无"])
    return "\n".join(lines) + "\n"


def build_profile(name: str, buckets: dict, stats: dict) -> str:
    core_traits = unique_keep_order(
        buckets["preferences"][:2] + buckets["values"][:2] + buckets["style_signals"][:2],
        6,
    )
    lines = [
        "# Profile",
        "",
        "## 一句话概述",
        f"{name} 的个人分身档案，强调真实、风格一致和可持续修正。",
        "",
        "## 这个人的核心特征",
    ]
    lines.extend([f"- {item}" for item in core_traits] or ["- 暂无"])
    lines.extend([
        "",
        "## 适合如何模拟",
    ])
    lines.extend([f"- {item}" for item in unique_keep_order(buckets["style_signals"][:3] + buckets["decision_signals"][:2] + buckets["emotion_signals"][:1], 6)] or ["- 暂无"])
    lines.extend([
        "",
        "## 不应如何模拟",
    ])
    lines.extend([f"- {item}" for item in unique_keep_order(buckets["anti_patterns"] + buckets["boundaries"][:3], 6)] or ["- 暂无"])
    lines.extend([
        "",
        "## 材料概况",
        f"- 共处理 {stats['record_count']} 条记录",
        f"- 来自 {stats['source_count']} 个来源：" + "、".join(f"{key}({value})" for key, value in stats["sources"].items()),
        "",
        "## 回答问题时的优先级",
        "1. 事实真实性",
        "2. 风格一致性",
        "3. 简洁程度",
    ])
    return "\n".join(lines) + "\n"


def write_me(output_dir: Path, name: str, records: list[dict]) -> None:
    buckets = classify_records(records)
    stats = collect_stats(records)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "versions").mkdir(exist_ok=True)
    (output_dir / "records.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    (output_dir / "self.md").write_text(build_self(name, buckets), encoding="utf-8")
    (output_dir / "persona.md").write_text(build_persona(buckets), encoding="utf-8")
    (output_dir / "profile.md").write_text(build_profile(name, buckets, stats), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a practical me profile from JSON records")
    parser.add_argument("inputs", nargs="+", help="Path(s) to input json records")
    parser.add_argument("--name", required=True, help="Me name or slug")
    parser.add_argument("--output-dir", default="selves", help="Output base directory")
    args = parser.parse_args()

    records = load_records([Path(item) for item in args.inputs])
    slug = slugify(args.name)
    output_dir = Path(args.output_dir) / slug
    write_me(output_dir, args.name, records)
    print(output_dir)


if __name__ == "__main__":
    main()
