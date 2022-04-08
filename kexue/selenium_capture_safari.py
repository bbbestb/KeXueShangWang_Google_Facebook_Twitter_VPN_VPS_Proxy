# -*- coding: utf-8 -*-

from selenium import webdriver
import time


def capture(url, img_file="test1.png"):
    safari = webdriver.Safari()
    safari.set_window_size(1200, 900)
    safari.get(url)
    safari.execute_script("""
        (function () {
            var y = 0;
            var step = 100;
            window.scroll(0, 0);

            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }

            setTimeout(f, 1000);
        })();
    """)

    for i in xrange(30):
        if "scroll-done" in safari.title:
            break
        time.sleep(1)

    safari.save_screenshot(img_file)
    safari.close()


if __name__ == "__main__":
    capture("http://smilejay.com/")
