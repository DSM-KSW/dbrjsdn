# DSM-KSW 프론트 앱과 리매핑 백그라운드

Windows에서 `main.py`를 실행하면 `backend_client.ensure_background()`가 리매핑 백엔드를 확인하고, 없으면 창 없는 자식 프로세스로 시작합니다. 프론트 창을 닫아도 백엔드는 계속 실행되며, 다음 실행 때 기존 프로세스의 Windows named pipe에 다시 연결합니다. 백엔드 소스는 `backend/` Git submodule로 포함됩니다. 저장소를 새로 받을 때 `git clone --recurse-submodules`를 사용하거나 `git submodule update --init`을 실행하세요.

프론트 코드에서 호출하는 방법:

```python
import backend_client

backend_client.set_binding([71], [17, 91, 37])  # G → Ctrl + Win + ←
backend_client.set_binding([], [65], mouse="마우스 X1")  # X1 → A
bindings = backend_client.list_bindings()
backend_client.delete_binding([71])
backend_client.call("set_active", active=False)
```

호출은 `backend/ipc.py`를 통해 JSON 바이트로 전달됩니다. 백엔드의 키보드 훅, 마우스 훅, IPC 수신기는 각각 독립 스레드입니다. 설정과 IPC 연결 키는 `%LOCALAPPDATA%\DSM-KSW`에 저장됩니다. 현재 프론트의 키보드 화면은 리매핑 추가·수정 UI가 아직 없으므로 위 호출 함수가 연동 지점입니다. 현재 출력은 키보드 조합만 지원합니다.

`main.spec`는 Flet 앱과 백엔드 DLL을 같은 Windows 실행 파일에 포함합니다. `pyinstaller main.spec`로 빌드합니다.
