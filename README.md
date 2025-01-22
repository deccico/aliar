# Avoid Spam with Infinite Email Aliases

This repository contains a Python-based solution for creating and managing infinite email aliases using the Namecheap API. It enables you to improve email privacy by forwarding emails from unique aliases to a single primary email address.

---

## Features
- Generate and manage email aliases automatically.
- Protect your primary email address from spam and profiling.
- Easy configuration using a single `credentials.py` file.
- Identify which service leaked your email.
- Disable aliases quickly if they become spammy.

---

## Getting Started

### Prerequisites
1. **Namecheap Account**: You need a domain registered with Namecheap for email forwarding.
2. **Python**: Install Python 3.7 or later.
3. **API Access**: Enable API access in Namecheap and whitelist your IP.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/deccico/aliar.git
   cd aliar
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your credentials in `credentials.py`:
   ```python
   api_user = 'your_namecheap_api_user'
   api_key = 'your_api_key'
   username = 'your_namecheap_username'
   client_ip = 'your_whitelisted_ip'
   domain = 'your-email-alias-domain.com'
   alias_email = 'your_primary_email_address'
   ```

---

## Usage

### Generate Aliases
Run the main script to create email aliases:
```bash
python aliar.py
```
The script will configure aliases (e.g., `1@yourdomain.com`, `2@yourdomain.com`) to forward emails to your primary email address.

### Custom Aliases
You can define custom aliases (e.g., `bank@yourdomain.com`) in the script for specific use cases.

---

## Limitations
1. **Replying to Emails**: Responses from aliases will appear to come from your primary email address unless you configure dedicated inboxes.
2. **IP Whitelisting**: Ensure your current IP address is whitelisted in Namecheap’s API settings.
3. **Delay**: Email forwarding might introduce slight delays, but they are generally negligible.

---

## Benefits
- Full control over your aliases and forwarding setup.
- Enhance privacy and reduce spam.
- Easily identify services that misuse your email address.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

