import mastering_pycharm_editor_section_service


def main():
    show_header()

    mastering_pycharm_editor_section_service.download_info()

    display_results()


def show_header():
    print("Welcome to the talking python info downloader")
    print()


def display_results():
    nmbr_episodes = mastering_pycharm_editor_section_service.download_info()

    print("number of episodes ", nmbr_episodes)
    start_range = 100
    end_range = start_range + nmbr_episodes

    for show_nmbr in range(int(start_range), int(end_range)):
        info = mastering_pycharm_editor_section_service.get_episode(show_nmbr - int(start_range))
        # print(info)
        print("{}. {} --> {}".format(info.show_id + 1, info.title, info.pubdate))


if __name__ == '__main__':
    main()
