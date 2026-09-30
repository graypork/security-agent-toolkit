from collections import Counter

def find_suspects(failed_users, threshold=2):
    counts = Counter(failed_users)
    suspects = []
    for user, count in counts.items():
        if count >= threshold:
            suspects.append(user)
    return suspects
