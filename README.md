# FastAPI Template

使用 FastAPI 建立的 RESTful API 模板專案。此專案同時支援使用標準 Python 虛擬環境的本地開發和 Zeabur 的部署環境。

<a href='https://zeabur.com/templates/MK8U02'><img src='https://zeabur.com/button.svg'/></a>

## 功能

- 基本的 FastAPI 應用程式結構
- 提供範例 API 端點，包括獲取隨機 S&P 500 股票資訊
- 支援本地開發與 Zeabur 部署

## API 端點

| 路徑 | 方法 | 說明 |
|------|------|------|
| `/` | GET | 返回歡迎訊息 |
| `/items/{item_id}` | GET | 返回指定 ID 的項目資訊 |
| `/api/getRandomSymbol` | GET | 返回一個隨機 S&P 500 股票的資訊 |

## 本地開發環境設定

### 使用標準 Python 虛擬環境

#### 1. 建立虛擬環境

```bash
python -m venv venv
```

#### 2. 啟動虛擬環境

在 macOS/Linux 上:

```bash
source venv/bin/activate
```

在 Windows 上:

```bash
venv\Scripts\activate
```

啟動後，你的命令提示字元前方應該會出現 `(venv)`。

#### 3. 使用 pip 安裝依賴

```bash
pip install -r requirements.txt
```

#### 4. 運行 FastAPI 應用程式

```bash
uvicorn main:app --reload
```

啟動後，你可以在瀏覽器中訪問:
- API 根路徑: http://127.0.0.1:8000
- API 文檔: http://127.0.0.1:8000/docs

#### 5. 離開虛擬環境

當完成工作後，可以使用以下命令離開虛擬環境:

```bash
deactivate
```

### 虛擬環境的優點

- 不需要安裝額外的套件管理器
- 與 requirements.txt 直接相容
- Python 標準庫支援，不依賴第三方工具
- 與 Zeabur 使用相同的依賴安裝方式 (pip install -r requirements.txt)

### 依賴管理

當你需要新增依賴時，可以先安裝然後更新 requirements.txt:

```bash
pip install <package_name>
pip freeze > requirements.txt
```

## 部署

此專案設定為使用 Zeabur 部署。點擊上方的部署按鈕即可在 Zeabur 上部署此專案。

## 授權

[MIT](LICENSE)
