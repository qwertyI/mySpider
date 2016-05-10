from scrapy.mail import MailSender


mailer = MailSender()
mailer.send(to=["727665171@qq.com"], subject="Some subject", body="Some body", cc=['727665171@qq.com'])
