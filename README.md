# ∆chat

temporary encrypted chat. open the site, get a link, send it to someone, chat

the link looks like `chat.delta.tf/?id#key`. everything after the `#` is the encryption key, and browsers never send that part to the server. messages get encrypted in your browser with AES-GCM before they leave, so the server only ever stores ciphertext.

## run it

    uv sync
    uv run python app.py

then open `localhost:8080`.

## how it works

- flask stores each room as a list of encrypted strings in memory
- all the crypto is javascript in `templates/chat.html` using the browser's web crypto api
- names are random and picked in your browser, so they don't prove who is typing
- wrong or missing key shows scrambled bytes and locks the composer

## limits

- nothing is saved to disk, restarting the server wipes every room
- anyone with the full link can read and write
- lose the link and the room is gone, nobody can recover the key
- the server can still see ip addresses, timing, and message sizes