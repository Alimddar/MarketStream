
```
product-app
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           └─ main
│  ├─ objects
│  │  ├─ 05
│  │  │  └─ e45431308d434d99ac48eabec88c56cbebc7c1
│  │  ├─ 06
│  │  │  └─ 2a79a263390cc4c4aaf922cf635c6d880a1ea9
│  │  ├─ 07
│  │  │  └─ 489da977a00ee58f10548d9b3112d9ec6f7244
│  │  ├─ 09
│  │  │  └─ 2fd51cbbf65eb6c646dc59564a41ab47edc1f2
│  │  ├─ 2e
│  │  │  └─ ea525d885d5148108f6f3a9a8613863f783d36
│  │  ├─ 2f
│  │  │  └─ 4c6b8a4dfc0da616f7ab186862f88aaf058ce3
│  │  ├─ 30
│  │  │  └─ f5d49484cdd2a3395451f8b17e05bb8074498c
│  │  ├─ 36
│  │  │  └─ 112a3c68590d6a8e07fea0ce70a5afb38c951a
│  │  ├─ 38
│  │  │  └─ 352a9a8f54c46b9d10d96303b2cad1e5b5ff95
│  │  ├─ 45
│  │  │  └─ 9817caba8de9dd944556d7b255a614c8b8cd7a
│  │  ├─ 46
│  │  │  └─ 7c127868f1570b6e33b9c308fae923df131884
│  │  ├─ 5c
│  │  │  └─ cc256047e3d2e3b3029336f131eeb7728c6094
│  │  ├─ 64
│  │  │  └─ 5aab28acb6d87641694602fdb217d33354e04b
│  │  ├─ 76
│  │  │  └─ 05f6fdac39f41533b6ba571dda24b99dcda0e1
│  │  ├─ 7c
│  │  │  └─ 4617d4f07f496a482486d980c79295c30dfd17
│  │  ├─ 84
│  │  │  └─ 6524feb4200680cbb5c42096eb620603896cd6
│  │  ├─ 98
│  │  │  └─ e4f9c44effe479ed38c66ba922e7bcc672916f
│  │  ├─ 9b
│  │  │  └─ 729983eb5fdb653f959da90d18ea48d414f9f3
│  │  ├─ a6
│  │  │  └─ 7ecfd08a1423532c0d504639beb631ea8db6ae
│  │  ├─ ac
│  │  │  └─ 4c2261ed5dbe79a0b7ffb135c02d2b0a05d281
│  │  ├─ b0
│  │  │  └─ abfb85334f1d568fd82e6f2ae435f0778e9dac
│  │  ├─ b2
│  │  │  └─ 7d7a08705151c3eb672766a5a35530a632f912
│  │  ├─ bb
│  │  │  └─ 25df8883715759220fb720c2e74b349b118969
│  │  ├─ c9
│  │  │  └─ dbcde9e9588532510c18fa15117ba19eb4f904
│  │  ├─ ce
│  │  │  └─ da0a5223917f6a705e0300a30558a7e9db4c5a
│  │  ├─ d6
│  │  │  └─ 875fadbd17e2ff210cb0456cf27ff48f250360
│  │  ├─ dd
│  │  │  └─ 465221dfd2dfa237f20a5d4059c0dcc53e9bd5
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  ├─ 045b976587b9c24346a198d53b2170ba13d316
│  │  │  ├─ 71fd602f9d4453d99a4b5c73458e3d9967d342
│  │  │  └─ 972ce8cebc2274fc2cc80b85adb950512c6048
│  │  ├─ f6
│  │  │  └─ 37d08d294a48d87c1f900b7e84e915ec959d84
│  │  ├─ fb
│  │  │  └─ c4b07dcef98b20c6f96b642097f35e8433258e
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ alembic.ini
├─ app
│  ├─ api
│  │  └─ v1
│  │     └─ enpoints
│  │        ├─ order.py
│  │        ├─ product.py
│  │        └─ user.py
│  ├─ core
│  │  ├─ config.py
│  │  └─ security.py
│  ├─ crud
│  │  ├─ crud_order.py
│  │  ├─ crud_product.py
│  │  └─ crud_user.py
│  ├─ dependencies
│  │  ├─ auth.py
│  │  └─ common.py
│  ├─ models
│  │  ├─ admin-panel-logs.py
│  │  ├─ chat.py
│  │  ├─ companies.py
│  │  ├─ order-items.py
│  │  ├─ order.py
│  │  ├─ product.py
│  │  ├─ screen-share.py
│  │  ├─ user.py
│  │  └─ video-call.py
│  ├─ schemas
│  │  ├─ order_schema.py
│  │  ├─ product_schema.py
│  │  └─ user_schema.py
│  ├─ services
│  │  ├─ export_service.py
│  │  └─ payment_service.py
│  ├─ static
│  │  ├─ css
│  │  └─ js
│  └─ templates
│     └─ login.html
├─ docker-compose.yml
├─ migrate.py
├─ migrations
│  ├─ README
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
└─ requirements.txt

```