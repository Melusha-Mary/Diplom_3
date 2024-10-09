def add_order(main_page, login_user): #Вспомогательный метод для создания заказа и получения его номера из окна подтверждения.
    main_page.add_ingredient_to_order(0)
    main_page.add_ingredient_to_order(3)
    main_page.click_place_order_button()
    main_page.wait_loading()
    order_number = main_page.get_order_number_from_confirm_popup()
    main_page.click_cross_button_in_popup_window()

    return order_number
