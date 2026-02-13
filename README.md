# OpenCode Kit

![Version](https://img.shields.io/badge/version-1.0-blue)
![Status](https://img.shields.io/badge/status-active-success)

## 概要

OpenCode Kit は、AI ネイティブ エージェント、スキル、およびコマンドシステムを使用した包括的な開発ワークスペースです。

### システム構成

- ✅ **48 個のスキル** / 48 domain-specific skills
- ✅ **21 個のエージェント** / 21 specialist agents
- ✅ **12 個のコマンド** / 12 custom commands
- ✅ **ユーティリティ スクリプト** / Utility scripts

## ディレクトリ構造

```
.
├── README.md                   # このファイル / This file
├── AGENTS.md                   # プロジェクト ルール / Project rules
├── opencode.json               # OpenCode 設定ファイル / Config
│
└── .opencode/                  # OpenCode ネイティブ設定 / Native config
    ├── agents/                 # 21 エージェント / 21 agents
    │   ├── orchestrator.md      # マルチエージェント調整
    │   ├── project-planner.md   # タスク計画
    │   ├── frontend-specialist.md
    │   ├── backend-specialist.md
    │   └── [18 その他 / 18 more]
    │
    ├── skills/                 # 48 スキル / 48 skills
    │   ├── nextjs-react-expert/    # React/Next.js 最適化
    │   ├── clean-code/             # コーディング標準
    │   ├── tailwind-patterns/      # Tailwind CSS
    │   ├── api-patterns/           # REST/GraphQL/tRPC
    │   ├── database-design/        # スキーマ設計
    │   ├── testing-patterns/       # テスト戦略
    │   └── [42 その他 / 42 more]
    │
    ├── commands/               # 12 コマンド / 12 commands
    │   ├── create.md            # 新しいアプリ作成
    │   ├── debug.md             # デバッグ
    │   ├── deploy.md            # デプロイ
    │   ├── test.md              # テスト
    │   ├── orchestrate.md       # マルチエージェント調整
    │   └── [7 その他 / 7 more]
    │
    ├── scripts/                # Python スクリプト / Python scripts
    │   ├── auto_preview.py
    │   ├── checklist.py
    │   └── verify_all.py
    │
    └── README_JA.md            # 詳細なドキュメント（日本語）
```

## クイック スタート

### 1. OpenCode を起動

```bash
opencode
```

### 2. ステータスを確認

```
/status
```

### 3. 最初のコマンドを試す

```
/plan simple-project
```

## 主な機能

### コマンド (12 個)

| コマンド | 説明 |
|---------|-------------|
| `/status` | プロジェクトの状態を表示 |
| `/plan` | タスク計画を作成 |
| `/create` | 新しいアプリケーションを構築 |
| `/enhance` | 既存のアプリに機能を追加 |
| `/debug` | 問題をデバッグ |
| `/test` | テストを実行 |
| `/deploy` | 本番環境にデプロイ |
| `/preview` | プレビュー サーバーを管理 |
| `/brainstorm` | アイデアを探索 |
| `/orchestrate` | マルチエージェントを調整 |
| `/ui-ux-pro-max` | UI/UX をデザイン |

### エージェント (21 個)

**プライマリ エージェント** (Tab キーで切り替え):
- `@orchestrator` - マルチエージェント調整
- `@project-planner` - タスク分解と計画

**スペシャリスト** (@ で呼び出し):
- `@frontend-specialist` - React/Next.js/UI
- `@backend-specialist` - Node.js/Python/API
- `@database-architect` - データベース設計
- `@security-auditor` - セキュリティ レビュー
- `@test-engineer` - テスト戦略
- `@devops-engineer` - CI/CD
- [他 15 個 / 15 more]

### スキル (48 個)

**フロントエンド**:
- `nextjs-react-expert` - React/Next.js 最適化 (57 ルール)
- `tailwind-patterns` - Tailwind CSS
- `web-design-guidelines` - UI/UX 監査 (100+ ルール)

**バックエンド**:
- `api-patterns` - REST/GraphQL/tRPC
- `database-design` - スキーマ設計
- `python-patterns` / `nodejs-best-practices`

**テストと品質**:
- `testing-patterns` - Jest/Vitest/pytest
- `systematic-debugging` - デバッグ手法
- `clean-code` - コーディング標準

## ドキュメント

詳細なドキュメントは [`.opencode/`](./.opencode/) ディレクトリを参照してください。

| ドキュメント | 説明 |
|-----------|-------------|
| [`.opencode/README_JA.md`](./.opencode/README_JA.md) | 詳細な使い方（バイリンガル） |
| [`AGENTS.md`](./AGENTS.md) | プロジェクト ルールとガイドライン |

## システム要件

- **OpenCode**: 最新版 / Latest version
- **Node.js**: 18+ (推奨 / recommended)
- **Python**: 3.8+ (スクリプト実行用 / for scripts)
- **OS**: Linux, macOS, Windows

## 参考文献

- **OpenCode Docs**: https://opencode.ai/docs/
- **GitHub**: https://github.com/anomalyco/opencode
- **Community**: https://opencode.ai/discord

---

**バージョン**: 1.0  
**最終更新**: 2026-02-13  
**ライセンス**: MIT License
