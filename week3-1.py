{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. 파이썬의 컴퓨팅 라이브러리, numpy\n",
    "**numpy를 이용해서 데이터를 다뤄봅시다!**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Our Goal\n",
    "1. Numpy 시작하기\n",
    "    - prerequisite : Python의 List\n",
    "    - numpy import하기\n",
    "    - numpy.array\n",
    "\n",
    "2. Numpy로 연산하기\n",
    "    - Vector - Scalar : elementwise! (+, -, *, /)\n",
    "    - Vector - Vector : elementwise / broadcasting (+, -, *, /)\n",
    "    - Indexing & Slicing\n",
    "3. Example : Linear Algebra with Numpy\n",
    "    1. basics\n",
    "    - 영벡터 : `.zeros()`\n",
    "    - 일벡터 : `.ones()`\n",
    "    - 대각행렬 : `.diag()`\n",
    "    - 항등행렬 : `.eye()`\n",
    "    - 행렬곱 : `@` / `.dot()`\n",
    "  \n",
    "    2. furthermore\n",
    "    - 트레이스 : `.trace()`\n",
    "    - 행렬식 : `.linalg.det()`\n",
    "    - 역행렬 : `.linalg.inv()`\n",
    "    - 고유값 : `.linalg.eig()`\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## I. Numpy 시작하기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## II. Numpy로 연산하기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## III. Numpy로 선형대수 지식 끼얹기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## IV. Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. 어떤 벡터가 주어졌을 때 L2 norm을 구하는 함수 `get_L2_norm()`을 작성하세요\n",
    "\n",
    "- **매개변수** : 1차원 벡터 (`np.array`)\n",
    "- **반환값** : 인자로 주어진 벡터의 L2 Norm값 (`number`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def get_L2_norm(array):\n",
    "    return np.linalg.norm(array, 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. 어떤 행렬이 singular matrix인지 확인하는 함수 `is_singular()` 를 작성하세요\n",
    "\n",
    "- 매개변수 : 2차원 벡터(`np.array`)\n",
    "- 반환값 : 인자로 주어진 벡터가 singular하면 True, non-singular하면 False를 반환 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def is_singular(array):\n",
    "    try:\n",
    "        np.linalg.det(array)\n",
    "    except:\n",
    "        return True\n",
    "    return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
