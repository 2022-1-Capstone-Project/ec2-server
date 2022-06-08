import sys
import time
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def to_sec(t):
    min, sec = t.rstrip().split(sep=":")
    return 60 * int(min) + int(sec)

def download_mp3(link, download_path):
    test_link = link 

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'download.default_directory': download_path}) # 저장할 경로 저장
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 에러 안뜨게 하는건데 뭔지 모름... 

    # 상황에 맞게 주석처리하면 될듯. 
    options.add_argument('--headless') # 화면 안뜨게 하는 것 
    options.add_argument('--no-sandbox') # ??
    options.add_argument('--disable-dev-shm-usage') #??

    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #driver = webdriver.Chrome(executable_path=settings.CHROMEDRIVER_PATH, options=options)
    '''
    맞는 executable_path 경로 설정해주세요
    '''
    #driver = webdriver.Chrome(executable_path="/home/ubuntu/face-your-pace-function/download/chromedriver",options=options)
    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    # selenium 4버전 부터 이런 식으로 sevice 변수로 여는 것을 권장하나봐요 찾아보니까 이렇게 나왔어요. 이렇게 작동 안되면 100번째 줄처럼 그냥 하시면 돼요






    #  ==================== 아래서부터는 같습니다 ================ xpath 절대경로..? 걍 해도 될듯
    # 링크열기
    download_link = 'https://soundcloudmp3.org/'
    driver.get(download_link)
    time.sleep(1)

    # 링크 입력
    input_xpath = '//*[@id="conversionForm"]/div/input[2]'
    driver.find_element(By.XPATH, value = input_xpath).click()
    driver.find_element(By.XPATH, value = input_xpath).send_keys(test_link)
    time.sleep(1)

    #다운로드 버튼 누르기  
    click_xpath = '//*[@id="conversionForm"]/div/span/button/span' # /html/body/div[2]/div[3]/div/div/div[1]/form/div/span/button/span
    driver.find_element(By.XPATH, value = click_xpath).click()
    driver.implicitly_wait(600)

    # title 정보 추출
    title_path = '/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/p[1]'
    title_xpath = driver.find_element(By.XPATH, value = title_path)
    title = title_xpath.text
    #print(title[6:])



    # length 정보 추출
    length_path = '/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/p[2]'
    length_xpath = driver.find_element(By.XPATH, value = length_path)
    length = length_xpath.text
    # print(length[7:-8])

    # image url 추출
    path = '/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/img'
    image_xpath = driver.find_element(By.XPATH, value = path).get_attribute("src")
    # print(image_xpath)

    #다운로드(하는) 버튼 누르기
    click_xpath = '//*[@id="download-btn"]' #/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[5]/a
    # download_link = driver.find_element(By.XPATH, value = click_xpath).get_attribute('href') # 다운로드 가능한 링크
    driver.find_element(By.XPATH, value = click_xpath).send_keys(Keys.ENTER) # 직접 버튼을 누르는 것
    time.sleep(15) # 서버가 좋으면 더 짧게 해도 가능
    driver.close()

    # filepath = download_path
    # filename = max([filepath + '\\' + f for f in os.listdir(filepath)], key=os.path.getctime)
    # shutil.move(os.path.join(filepath, filename), new_filename)

    '''
    bpm 까지 추출하도록 하면 여기서 진행되어야 함. 
    y, sr = librosa.load(ownload_path, sr= 96000) # 다운로드 한 위치로
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
    str(tempo)
    '''

    # 노래 제목, 재생 길이, 커버사진을 $ 를 구분자로 return
    #print(title[6:]+'<>'+str(to_sec(length[7:-8]))+'<>'+image_xpath)
    print(title[6:].strip()+'<>'+str(to_sec(length[7:-8]))+'<>'+image_xpath)
    #return (title[6:]+'<>'+str(to_sec(length[7:-8]))+'<>'+image_xpath)
    return (title[6:].strip()+'<>'+str(to_sec(length[7:-8]))+'<>'+image_xpath)

    

if __name__ == '__main__':
    link = sys.argv[1]
    download_path = sys.argv[2] 

    # print('C:\\Users\\yoondain\\Desktop\\capstone' == r'C:\Users\yoondain\Desktop\capstone')
    # print(link)
    # print(download_path)
    a = download_mp3(link,download_path)
    #print(a)

    # download_mp3('https://soundcloud.com/ferret-lie/only-your-stars-trickstar-ver',r'C:\Users\yoondain\Desktop\capstone')
