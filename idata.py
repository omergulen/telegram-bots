from playwright.sync_api import sync_playwright
from constants import USER_BROWSER_SESSION_PATH, HEADLESS, TELEGRAM_CHAT_ID
from tg import sendMessage

def hunt():
    activityURL = 'https://deu-schengen.idata.com.tr/tr/appointment-form'

    with sync_playwright() as p:
        # browser = p.chromium.launch_persistent_context(
        #     USER_BROWSER_SESSION_PATH, headless=HEADLESS, color_scheme='dark', locale='en-GB', viewport={'width': 1024, 'height': 720}, device_scale_factor=2)

        browser = p.chromium.launch_persistent_context(USER_BROWSER_SESSION_PATH, headless=HEADLESS, is_mobile=True, color_scheme='dark', locale='en-GB',
                                                       user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1', viewport={'width': 390, 'height': 844}, device_scale_factor=2)

        page = browser.new_page()
        page.goto(activityURL)
        page.wait_for_load_state('domcontentloaded')
        # page.pause()

        page.locator("#city").select_option("6")
        page.locator("#office").select_option("2")
        page.locator("#officetype").select_option("1")
        page.locator("#totalPerson").select_option("1")
        page.get_by_role("link", name="İLERİ ").click()
        page.get_by_role("textbox", name="İsim (*)").fill("ALI")
        page.get_by_role("textbox", name="Soyisim (*)").fill("VELI")
        page.locator("#birthday1").select_option("01")
        page.locator("#birthmonth1").select_option("01")
        page.locator("#birthyear1").select_option("1990")
        page.get_by_role("textbox", name="Pasaport No (*)").fill("U11111111")
        page.get_by_role("textbox", name="Telefon (*)").fill("5555555555")
        page.get_by_role("textbox", name="Email (*)").fill("citizenkane@gmail.com")
        page.get_by_role("link", name="İLERİ ").click()
        page.get_by_role("link", name="İLERİ ").click()
        page.locator("#flightDate span").click()
        page.get_by_role("cell", name="»").click()
        page.get_by_role("cell", name="31").click()

        aprilRows = ['3 4 5 6 7 8 9', '10 11 12 13 14 15 16',
                     '17 18 19 20 21 22 23', '24 25 26 27 28 29 30']
        mayRows = ['1 2 3 4 5 6 7', '8 9 10 11 12 13 14',
                   '15 16 17 18 19 20 21', '22 23 24 25 26 27 28', '29 30 31']

        counter = 0
        rows = [[aprilRows, 4], [mayRows, 5]]
        for activeRowArr in rows:
            month = activeRowArr[1]
            activeRowArr = activeRowArr[0]
            for row in activeRowArr:
                days = row.split(' ')
                for day in days:
                    try:
                        page.locator("#datepicker span").click()
                        page.get_by_role("row", name=row).get_by_role(
                            "cell", name=day).click()
                        page.wait_for_load_state('networkidle')
                        notFoundElement = page.get_by_text(
                            "Seçtiğiniz tarihte uygun randevu saati bulunmamaktadır.")
                        if notFoundElement:
                            print('{}.{}.2023 - not found'.format(day, month))
                        else:
                            text = '{}.{}.2023 - could be'.format(day, month)
                            sendMessage(text, TELEGRAM_CHAT_ID)
                            counter += 1
                            print(text)
                    except:
                        continue

        if counter == 0:
            sendMessage('No appointment found', TELEGRAM_CHAT_ID)
        browser.close()

    # postTitle = page.locator("[data-adclicklocation='title']")
    # postTitle.evaluate("node => node.style.padding = '16px'")
    # postTitle.screenshot(path=rootPath + '0.jpeg')

    # browser.close()
    # browser = p.chromium.launch_persistent_context(USER_BROWSER_SESSION_PATH, headless=HEADLESS, is_mobile=True, color_scheme='dark', locale='en-GB',
    #                                                user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1', viewport={'width': 390, 'height': 844}, device_scale_factor=2)

    # page = browser.new_page()
    # page.goto(activityURL)
    # page.wait_for_load_state('domcontentloaded')

    # try:
    #     page.wait_for_selector('.nightMode')
    # except:
    #     page.get_by_role("button", name="Settings").click()
    #     page.locator("label").filter(
    #         has_text="Dark mode").locator("svg").click()
    #     page.locator(".MobileButton").click()
    #     page.wait_for_selector('.nightMode', timeout=5000)

    # article = page.locator('.PostHeader__post-title-line').inner_text()
    # content = [article]

    # try:
    #     page.wait_for_selector(
    #         "View this NSFW content anonymously in the Reddit appWhile Anonymous Browsing, yo", timeout=5000)
    #     print('NSFW warning.')
    #     page.get_by_role("button", name="Not now").click()
    #     print('NSFW warning closed.')
    # except:
    #     print('No NSFW warning.')

    # try:
    #     page.wait_for_selector('.XPromoPopupRpl__header', timeout=5000)
    #     print('App modal.')
    #     actions = page.locator('.XPromoPopupRpl__action')
    #     continueButton = actions.get_by_role(    #         'button', name="Continue").click()
    #     print('App Modal closed.')
    # except:
    #     print('No App Modal.')

    # page.wait_for_selector('.PostContent__selftextContainer')
    # counter = 1
    # for comment in page.locator('.PostContent__selftextContainer p').all():
    #     comment.scroll_into_view_if_needed()
    #     commentBody = comment.inner_text().replace(    #         "\n\n\n", "\n").replace("\n\n", "\n")
    #     print('commentBody: ' + str(commentBody))
    #     print('commentBody len: ' + str(len(commentBody)))
    #     if len(commentBody) < 2:
    #         continue

    #     content.append(commentBody)

    #     comment.evaluate("node => node.style.padding = '16px'")
    #     path = rootPath + str(counter) + '.jpeg'
    #     comment.screenshot(path=path, scale='device',
    #                        type='jpeg', quality=100)
    #     counter += 1

    browser.close()
    # f = open(rootPath + 'content', 'w')
    # f.write("\n".join(content))
    # f.close()


hunt()
