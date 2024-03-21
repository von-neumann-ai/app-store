"""Replace strings in a file with random"""

import sys
import secrets


def gen_random_string():
    return secrets.token_urlsafe(16)


def main(env_file):
    with open(env_file) as f:
        env = f.read()

    env_dict = {}
    for line in env.split("\n"):
        if not (line.startswith("#") or line.strip() == ""):
            k, v = line.split("=")
            env_dict[k] = v

    generated_passwords = {
        v: gen_random_string() for v in env_dict.values() if v.startswith("generate_me")
    }

    env_dict = {k: generated_passwords.get(v, v) for k, v in env_dict.items()}
    
    env_gen = "\n".join(f"{k}={v}" for k, v in env_dict.items())
    with open(env_file + '.gen', 'w') as f:
        f.write(env_gen)


if __name__ == "__main__":
    main(sys.argv[1])
