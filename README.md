# ScreenC 📸

Screen Cloud is a solution crafted to address challenges faced by Iranian users experiencing difficulties in sending media content on platforms with filtered or restricted CDNs (Content Delivery Networks), such as Discord. This project leverages Amazon S3 (Simple Storage Service) to empower users to upload their content seamlessly, bypassing the need for VPNs or third-party services.

## Key Features

- **Effortless Uploads:** Easily upload media content to Amazon S3 without the reliance on VPNs or external services.

- **CDN Bypass:** Circumvent CDN restrictions on various platforms, ensuring smooth media sharing experiences.

- **Secure Storage:** Utilize the security and reliability of Amazon S3 for storing uploaded content.

## How It Works

1. Users take their screen shot using GUI app . 

2. The uploader securely transfers the png to Amazon S3.

3. Uploaded file url will be replaced instead of png in clipboard.

4. Share the links on platforms with restricted CDNs, enabling others to access the media seamlessly.

## Getting Started

### Prerequisites

- Python installed 
- Amazon S3 account with credentials

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/blackaleader/ScreenC.git
   ```
2. Activate the venv

```sh
venv\scripts\Activate
```

3. Install required libraries
```sh
pip install -r requirements.txt
```

4. Run the script
```sh
python main.py
```
```sh
python3 main.py
```

## Authors

- [@ArmanLeader](https://github.com/blackaleader) 😎
- [@Tears](https://github.com/Ohtears) 💧



