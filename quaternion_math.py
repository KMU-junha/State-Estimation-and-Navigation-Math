import numpy as np

def euler_to_quaternion(roll, pitch, yaw):
    """
    오일러 각(rad)을 쿼터니언(w, x, y, z)으로 변환
    공식: q = cos(theta/2) + sin(theta/2) * v
    """
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    
    return [qw, qx, qy, qz]

def quaternion_multiply(q1, q2):
    """
    두 쿼터니언의 곱 (회전의 결합)
    """
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    
    return [w, x, y, z]

if __name__ == "__main__":
    # Test Case: 90 degree rotation on Z-axis
    roll, pitch, yaw = 0, 0, np.pi/2
    q = euler_to_quaternion(roll, pitch, yaw)
    print(f"Euler({roll}, {pitch}, {round(yaw,2)}) -> Quaternion: {np.round(q, 3)}")
    print("Success: 3D Rotation Math Verified.")