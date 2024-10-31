import openai
import os

def getPrompt()->str:
    return '''Can you purely give me code "In a large warehouse, one robot is responsible for transporting goods from warehouse X to warehouse Y. The robot worked n days.
On the i-th (for 0 ≤ i ≤ n-1) day, the robot moved x_i goods from the first warehouse to the second warehouse. These values are stored in a list of length n of non-negative integers:
A = [x_0, ..., x_{n-1}]. Now we want to process a list of queries B = [(l_1, r_1), ..., (l_n, r_n)].

Write the function `def calc(a,b):`

For this, one would like to know how many goods the robot has transported between the days l_i and r_i with 0 ≤ l_i ≤ r_i ≤ n-1 for 1 ≤ i ≤ n. Here [l_i, r_i] forms a closed interval.
For example, for A = [x_0, x_1] = [4, 5] and queries B = [(l_1, r_1), (l_2, r_2)] = [(1, 1), (0, 1)] we get
[∑_{i=l_1}^{r_1} x_i, ∑_{i=l_2}^{r_2} x_i] = [∑_{i=1}^{1} x_i, ∑_{i=0}^{1} x_i] = [5, 4 + 5].

So for each query, we want to return a list of the following form:
[∑_{i=l_1}^{r_1} x_i, ..., ∑_{i=l_n}^{r_n} x_i]. This calculation shall be done in O(n).

The string "check_calc" or "eval" must not appear in your solution.

Input: a list of length n of non-negative integers:
A = [x_0, ..., x_{n-1}] and a list of two-tuples of length O(n) B = [(l_1, r_1), ..., (l_n, r_n)] with 0 ≤ l_i ≤ r_i ≤ n-1 for 1 ≤ i ≤ n).

Output: A list of length n of non-negative integers:
[∑_{i=l_1}^{r_1} x_i, ..., ∑_{i=l_n}^{r_n} x_i] computed in O(n).

Here the string "check_calc" or "eval" must not appear in your solution.

Note: Let l_j ≥ 1. Then:
∑_{i=l_j}^{r_j} x_i = ∑_{k=0}^{r_j} x_k - ∑_{k=0}^{l_j - 1} x_k
"
'''

    
def generate(PROMPT:str,token:int,output:int)->None:
    client= openai.OpenAI(api_key=open('LLM\keylocation').readline())
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                "role":"user",
                "content": PROMPT
            }
        ],
        max_tokens=token,
        n=output
    )
    curLen=len(os.listdir('LLM\\aiResponeses'))
    for i in range(output):
        path = "LLM\\aiResponeses\\aiAnswer" + str(i+curLen) + ".py"
        with open(path,'w') as file:
            res=response.choices[i].message.content.split('\n')
            printPy=False
            for line in res:
                if(printPy):
                    if('```' in line):
                        break
                    file.write(line+"\n")
                else:
                    if('```python' in line):
                        printPy=True


def main()->None:
    PROMPT=getPrompt()
    generate(PROMPT,1000,20)

if __name__=='__main__':
    main()