import password_cracker
from unittest import main

def test_hashes():
    test_cases = [
        ("b305921a3723cd5d70a375cd21a61e60aabb84ec", "sammy123", False),
        ("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e", "abacab", False),
        ("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", "password", False),
        ("53d8b3dc9d39f0184144674e310185e41a87ffd5", "superman", True),
        ("da5a4e8cf89539e66097acd2f8af128acae2f8ae", "q1w2e3r4t5", True),
        ("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", "bubbles1", True)
    ]

    for hash, expected_password, use_salts in test_cases:
        result = password_cracker.crack_sha1_hash(hash, use_salts)
        print(f"Hash: {hash} \nDeve retornar: \"{expected_password}\" \nResultado: \"{result}\"\n")

if __name__ == "__main__":
    test_hashes()
    
    # Run unit tests automatically
    main(module="test_module", exit=False)
