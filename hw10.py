import os
import pickle

def input_scores():
    l = []
    n = 1

    print("[점수 입력]")
    while True:
        r = int(input(f"#{n}? "))
        n+=1
        l.append(r)
        
        if r < 0:
            l.pop()
            break
    return l

def get_average(l):
    avg = sum(l)/len(l)
    return avg

def show_scores(l):
    print("개인점수:", end="")
    for i in l:
        print(i,end=" ")



def save_data(scores):
    with open(filename, "wb") as file:
        pickle.dump(scores, file)

def load_data():
    with open(filename, "rb") as file:
        scores = pickle.load(file)

    return scores



filename = "score.bin"

if os.path.exists(filename):
    r_scores = load_data()
    print("\n[파일 읽기]")
    print("\n[점수 출력]")
    show_scores(r_scores)
    print(f"\n평균:{get_average(r_scores):.1f}")

else:
    list = input_scores()
    print("\n[점수 출력]")
    show_scores(list)
    print(f"\n평균:{get_average(list):.1f}")
    save_data(list)
    