import platform, socket, sys
from datetime import datetime

print("[과제2] Git 배포 실행 테스트")
print("실행 호스트:", socket.gethostname())
print("운영체제:", platform.platform())
print("파이썬 버전:", sys.version.split()[0])
print("실행 시각:", datetime.now())