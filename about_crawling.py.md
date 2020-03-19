>>>가게 창을 열어놓고 원래 창에서만 활동함ㅠ
https://devyurim.github.io/python/crawler/2018/08/13/crawler-3.html
새롭게 열린 탭으로 변경하는 코드는 아래의 코드를 추가하면 된다.
# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])
# 로딩 기다리기
time.sleep(5)

만약에 새로 옮긴 탭을 닫고 다시 원래 창으로 돌아가고 싶다면 아래의 코드를 입력하면 된다.
# 현재 탭 닫기
driver.close()
# 맨 처음 탭으로 변경(0번 탭)
driver.switch_to.window(driver.window_handles[0])
# 로딩 기다리기
time.sleep(5)



+++
driver.implicitly_wait(3)