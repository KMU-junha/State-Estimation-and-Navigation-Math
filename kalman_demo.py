iimport numpy as np
import matplotlib.pyplot as plt

def kalman_filter_demo():
    # 1. 초기값 설정
    dt = 0.1
    n_steps = 100
    
    # 실제 위치 (True State)
    t = np.linspace(0, 10, n_steps)
    true_position = np.sin(t) 
    
    # 측정값 (Measurement with Noise)
    measurement_noise = 0.2
    measurements = true_position + np.random.normal(0, measurement_noise, n_steps)
    
    # 칼만 필터 변수 초기화
    x_est = 0.0      # 초기 추정값
    P = 1.0          # 초기 오차 공분산
    Q = 0.01         # 시스템 노이즈 공분산 (Process Noise)
    R = measurement_noise ** 2 # 측정 노이즈 공분산 (Measurement Noise)
    
    estimates = []
    
    # 2. 칼만 필터 루프 (Prediction -> Update)
    for z in measurements:
        # A. 예측 (Prediction)
        x_pred = x_est
        P_pred = P + Q
        
        # B. 업데이트 (Update)
        K = P_pred / (P_pred + R)  # 칼만 게인 (Kalman Gain)
        x_est = x_pred + K * (z - x_pred) # 상태 추정
        P = (1 - K) * P_pred       # 오차 공분산 업데이트
        
        estimates.append(x_est)
        
    # 3. 결과 시각화
    plt.figure(figsize=(10, 6))
    plt.plot(t, true_position, 'g--', label='True Position')
    plt.scatter(t, measurements, c='r', s=10, label='Noisy Measurements')
    plt.plot(t, estimates, 'b-', linewidth=2, label='Kalman Filter Estimate')
    plt.title('Kalman Filter: Signal Denoising Demo')
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.legend()
    plt.grid(True)
    plt.savefig('kalman_result.png') # 결과 이미지 저장
    print("Result saved as kalman_result.png")

if __name__ == "__main__":
    kalman_filter_demo()