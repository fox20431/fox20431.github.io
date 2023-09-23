---
title: Cloudflare WARP for linux
excerpt: WARP uses the VPN tech and bases on WireGurad.
---

# Cloudflare WARP For Linux

reference: https://mailberry.com.cn/2023/02/cf-solve-it-completely-error-code-1020-by-warp/

## Why do we need WARP

Unlocked the ChatGPT, and so on.

Next, I will tell a specific case to facilitate our deeper understanding.

As we all know, ChatGPT blocks all Chinese IPs and almost all VPS IPs which is in order to prevent Chinese users from using VPS as the VPN.

We need the IP which has the correct attribution(such as the IP address that comes from JP) and is not in the block list. 

First, we can rent a Japanese VPS to get a Japanese IP, then how to resolve the question of the block list. We can use another IP to proxy the Japanese IP. Who can do it? Cloudflare WARP!

You may question my solution; why not just use Cloudflare WARP directly, but rent the server first? Because the Cloudflare WARP just provides a new IP where the origin IP is.

## Setup

1. Config the package repository

   reference: https://pkg.cloudflareclient.com

2. Install the package

    ```sh
    apt install cloudflare-warp
    ```

3. Register for WARP

   ```
   warp-cli register
   ```

4. Open VPN

   ```
   warp-cli set-mode proxy
   ```

5. Connect the WARP

   ```
   warp-cli connect
   ```

6. Check

   ```
   curl ifconfig.me --proxy socks5://127.0.0.1:40000
   ```

   It will display the IP on the screen.

7. (Optional) You can use the following command to test whatever website you want to test.

   ```
   curl https://chat.openai.com/ --proxy socks5://127.0.0.1:40000
   ```

   
