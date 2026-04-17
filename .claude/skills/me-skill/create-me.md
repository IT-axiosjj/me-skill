# create-me

当用户要求“创建一个 me”时，执行以下流程：

1. 询问名称/代号
2. 询问用途
3. 询问是否已有原始材料
4. 若没有材料，则按 `prompts/intake.md` 继续访谈
5. 若已有材料，则引导用户导入并生成
6. 最终输出：
   - `selves/<slug>/self.md`
   - `selves/<slug>/persona.md`
   - `selves/<slug>/profile.md`

优先保证结果真实、可修正、不过度表演。
