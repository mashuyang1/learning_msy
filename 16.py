from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

Email = 'test@tset.com'
password = '123456'


class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = Email
        self.password = password

    def get_geetest_button(self):
        """
        获取geetest的按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        获取验证码的位置
        :return: 验证码位置元祖
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'],\
                                   location['x'] + size['width']
        return top, bottom, left, right

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :param name:
        :return:图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

    def get_screenshot(self):
        pass

    def get_slider(self):
        """
        获取滑块
        :return:
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    # 点按呼出缺口
    slider = get_slider()
    slider.click()

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance:
        :return:
        """
        #  移动轨迹
        track = []
        #  当前位移
        current = 0
        #  减速阀值
        mid = distance * 4/5
        #  计算间隔
        t = 0.2
        #  初速度
        v = 0

        while current < distance:
            if current < mid:
                a = 2      #  当位置小于减速阀值时，加速的a为正值
            else:
                a = -3       #  当前位移大于阀值时，加速度a为负值
            v0 = v
            move = v0 + 1/2 * a * t * t
            v = v0 + a * t
            current += move
            track.append(round(move))
        return track

    def move_to_gap(self, slider, tracks):
        """
        拖到滑块到缺口处
        :param slider:滑块
        :param tracks:轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()