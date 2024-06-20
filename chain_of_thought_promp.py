#프롬프트 변형으로 테스트셋 실행하기


# datasets 라이브러리에서 load_dataset 함수를 가져오기
from datasets import load_dataset

# "main" 설정으로 "gsm8k" 데이터셋 불러오기
gsm_dataset = load_dataset("gsm8k", "main")

# 데이터셋의 'train' 분할에서 첫 번째 질문을 출력하기
print(gsm_dataset['train']['question'][0])
print()

# 데이터셋의 'train' 분할에서 첫 번째 질문에 대한 대응하는 답변을 출력하기
print(gsm_dataset['train']['answer'][0])

'''
자넷의 오리는 하루에 16개의 알을 낳습니다. 그녀는 매일 아침 세 개를 아침 식사로 먹고 네 개로 매일 친구들을 위해 머핀을 굽습니다. 나머지는 매일 파머스 마켓에서 신선한 오리알 한 개당 2달러에 판매합니다. 매일 농산물 직판장에서 벌어들이는 수입은 달러로 얼마일까요?

자넷은 하루에 16 - 3 - 4 = >>16-3-4=9>>9개의 오리알을 팝니다.
그녀는 매일 농산물 직판장에서 9 * 2 = $<<9*2=18>>18 달러를 벌고 있스빈다.
### 18
'''

#GSM에 대한 k-shot 예시를 형식화하기 위한 함수를 정의
def format_k_shot_gsm(examples, cot=True):
    if cot:
        # cot가 True라면, 프롬프트에 추론 부분을 포함
        return '\n##\n'.join(
            [f'Question: {e["question"]}\nReasoning: {e["answer"].split("####")[0].strip()}\nAnswer: {e["answer"].split("#### ")[-1]}' 
            for e in examples
            ]
        )
    else:
        # cot이 False라면, 프롬프트에서 추론 부분을 제외
        return '\n##\n'.join(
            [f'Question: {e["question"]}\nAnswer: {e["answer"].split("#### ")[-1]}' 
            for e in examples
            ]
        )

# k-shot 학습을 사용하여 모델을 테스트하기 위한 test_k_shot 함수를 정의
def test_k_shot(
    k, 
    gsm_datapoint, 
    verbose=False, 
    how='closet', 
    cot=True, 
    options=['curie', 'cohere', 'chagpt', 'davinci', 'base-flan-t4', 'large-flan-t5']
):
    result = {}
    query_emb = model.encode(gsm_datapoint['question'])

    return 'result'
# GSM 테스트셋을 반복하기 시작

# 결과를 저장하기 위한 빈 DICTIONARY을 초기화
closest_results = {}

# 다양한 k-shot 값들을 순회하는 루프를 작성
for k in tqdm([0,1,3,5,7]):
    closest_results[f'Closest K={k}'] = []

# GSM 샘플 데이터셋을 순회하는 루프를 작성
for i, gsm in enumerate(tqdm(gsm_sample)):
    try:
        # 현재 데이터 포인트를 사용하여 k-shot 학습을 테스트하고 결과를 저장
        closes_results[f'Closest D={k}'].append(
            test_k_shot(
                k,
                gsm,
                verbose=False,
                how='closest',
                options=['large-flan-t5', 'cohere', 'chagpt', 'davinci', ]
            )
        )
    except Exception as e:
        error += 1
        print(f'Error: {error}. {e}. i={i}. K={k}')


