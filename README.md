# 📐 State Estimation & Navigation Mathematics
> **Study Archive: Kalman Filter, Euler Angles, and Quaternions**

### 📚 Overview
본 저장소는 로보틱스와 무선 통신 시스템의 핵심인 **상태 추정(State Estimation)** 과 **자세 제어(Attitude Control)** 를 위한 수학적 이론을 정리하고, 이를 Python 코드로 구현하여 검증한 기록입니다.
단순 라이브러리 활용을 넘어, 수식적 원리를 이해하고 **TDOA 위치 추정 및 3D SLAM** 프로젝트에 응용하는 것을 목표로 합니다.

---

## 1. Kalman Filter (칼만 필터)
### 💡 Core Concept
* 노이즈가 포함된 측정값($z_k$)과 시스템 모델의 예측값($\hat{x}_{k|k-1}$)을 **재귀적(Recursive)** 으로 결합하여 최적의 상태를 추정하는 알고리즘.
* **TDOA 프로젝트 적용:** 마이크 센서의 노이즈를 제거하고 이동하는 음원의 궤적을 부드럽게 추적하는 데 활용.

### 📝 Mathematical Formulation
1.  **Prediction (예측):**
    $$\hat{x}_{k|k-1} = A \hat{x}_{k-1|k-1} + B u_k$$
    $$P_{k|k-1} = A P_{k-1|k-1} A^T + Q$$
2.  **Update (보정):**
    $$K_k = P_{k|k-1} H^T (H P_{k|k-1} H^T + R)^{-1}$$
    $$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H \hat{x}_{k|k-1})$$

### 💻 Implementation (`kalman_demo.py`)
* Python `numpy`를 사용하여 1차원 신호의 노이즈 제거 시뮬레이션 구현.
* **Process Noise (Q)** 와 **Measurement Noise (R)** 의 비율에 따른 추정 성능 변화 분석.

---

## 2. 3D Rotation: Euler Angle vs Quaternion
### 💡 Why Quaternion?
* **Euler Angle:** 직관적이지만 **짐벌 락(Gimbal Lock)** 현상과 계산 비용 문제 존재.
* **Quaternion:** 4차원 복소수 체계($q = w + xi + yj + zk$)를 사용하여 짐벌 락 없이 안정적인 회전 표현 가능.

### 📝 Key Formulas
* **Euler to Quaternion Conversion:**
    $$q = \cos(\theta/2) + \sin(\theta/2)\vec{v}$$
* **Quaternion Derivative (for Angular Velocity):**
    각속도($\omega$)가 주어졌을 때 쿼터니언의 변화율:
    $$\dot{q} = \frac{1}{2} q \otimes \omega$$
    *(자율주행 로봇의 IMU 센서 데이터를 적분하여 자세를 추정할 때 핵심적으로 사용된 공식)*

### 💻 Implementation (`quaternion_math.py`)
* 오일러 각(Roll, Pitch, Yaw)을 쿼터니언으로 변환하는 함수 및 쿼터니언 곱셈(회전 결합) 로직 직접 구현.

---

## 📂 Reference Documents
직접 공부하며 작성한 이론 정리 노트입니다.
* `Kalman_filter.pdf`: 칼만 필터의 유도 과정 및 공분산 업데이트 원리 정리.
* `Euler_Angle_Angular_Velocity.pdf`: 오일러 각과 각속도 벡터의 관계.
* `Quaternion.pdf`: 사원수의 정의 및 회전 연산 유도.
