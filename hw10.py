import os
import pickle

FILENAME = "score.bin"

def input_scores():
    scores = []
    i = 1
    while True:
        raw = input(f"#{i}? ")
        if not raw.strip():
            break
        try:
            score = int(raw)
            if score < 0:
                break
            scores.append(score)
            i += 1
        except ValueError:
            print("정수를 입력하세요.")
    return scores

def get_average(scores):
    return sum(scores) / len(scores) if scores else 0

def show_scores(scores):
    print("개인점수:", *scores)
    print("평균: {:.1f}".format(get_average(scores)))

def save_scores(scores):
    with open(FILENAME, "wb") as f:
        pickle.dump(scores, f)

def load_scores():
    with open(FILENAME, "rb") as f:
        return pickle.load(f)

def main():
    if os.path.exists(FILENAME):
        print("[파일 읽기]")
        scores = load_scores()
    else:
        scores = input_scores()
        save_scores(scores)

    if scores:
        show_scores(scores)

if __name__ == "__main__":
    main()
