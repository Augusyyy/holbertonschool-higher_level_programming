def generate_invitations(template, attendees):
    # 检查模板是否为字符串
    if not isinstance(template, str):
        print("错误：模板应为字符串类型。")
        return

    # 检查参与者是否为字典组成的列表
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("错误：参与者应为字典组成的列表。")
        return

    # 检查模板是否为空
    if template.strip() == "":
        print("模板为空，未生成任何文件。")
        return

    # 检查参与者列表是否为空
    if not attendees:
        print("没有提供数据，未生成任何文件。")
        return

    # 遍历每一个参与者，生成个性化邀请函
    for idx, attendee in enumerate(attendees, start=1):
        # 创建模板的副本
        invitation = template[:]

        # 替换模板中的占位符
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:  # 如果值为 None，则替换为 "N/A"
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # 生成输出文件名
        output_filename = f"output_{idx}.txt"
        # 将邀请函写入文件
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

        print(f"生成了文件 {output_filename}")


# 示例用法
if __name__ == "__main__":
    # 从文件读取模板内容
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # 参与者列表
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20",
         "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # 调用函数生成邀请函
    generate_invitations(template_content, attendees)