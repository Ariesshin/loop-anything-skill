# Evidence Log

# 证据日志

Experiment 03 is now `Receipt splitter reliability` / `账单拆分工具可靠性`.

## Reproduction commands / 复现命令

Baseline:

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/control/receipt_splitter.py --format markdown
```

Final:

```bash
python3 experiments/readme-before-after-suite/experiments/03-receipt-splitter/materials/run_receipt_splitter_tests.py --impl experiments/readme-before-after-suite/experiments/03-receipt-splitter/runs/loop/final.py --format markdown
```

## Results / 结果

- Baseline: 5/11 tests, raw score 25/55, normalized score 45.5/100.
- Loop final: 11/11 tests, raw score 55/55, normalized score 100.0/100.

## Notes / 说明

The shell output showed the full test results. A local zsh status hook returned a post-command `dump_zsh_state` error in one run, so the evidence relies on the complete printed test output and the deterministic test files saved in this directory.

终端输出已完整显示测试结果。其中一次运行在命令结束后触发本地 zsh 状态钩子 `dump_zsh_state` 错误，因此证据以完整打印出的测试结果和本目录保存的确定性测试文件为准。