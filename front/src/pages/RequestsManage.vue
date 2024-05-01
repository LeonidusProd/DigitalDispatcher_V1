<template>
  <div class="container">
    <div class="left-side-menu">
      <div class="up-block">
        <div class="logo-block">
          <img class="logo-img" src="@/assets/Лого%20текст%20снизу.svg" alt="logo">
        </div>
        <div class="menu-block">
          <div class="menu-button active-button">
            Новые заявки
          </div>
          <div class="menu-button">
            Активные заявки
          </div>
        </div>
      </div>
      <div class="down-block">
        <my-button class="exit-button">Выход</my-button>
      </div>


    </div>

    <div class="workspace">
      <div class="requests-list">
        <h4>Новые заявки</h4>
        <div class="requests-list-scroll custom-scroll">
          <ShortRequestCard date="Заявка от 23.04.2024 в 16:00"
                            adress="Ул. Пупина, д. 13"
                            info="Нет света"
                            class="">
          </ShortRequestCard>

          <ShortRequestCard date="Заявка от 23.04.2024 в 14:20"
                            adress="Ул. Волжская, д. 74"
                            info="Разбитое стекло в 3 подьезде"
                            class="active-button">
          </ShortRequestCard>

          <ShortRequestCard date="Заявка от 23.04.2024 в 13:10"
                            adress="Ул. Борская, д. 18"
                            info="Протекает полотенцесушитель"
                            class="">
          </ShortRequestCard>

          <ShortRequestCard date="Заявка от 23.04.2024 в 12:50"
                            adress="Ул. Окская, д. 20"
                            info="Переполнены мусорные баки"
                            class="">
          </ShortRequestCard>
          <ShortRequestCard date="Заявка от 23.04.2024 в 12:50"
                            adress="Ул. Окская, д. 20"
                            info="Переполнены мусорные баки"
                            class="">
          </ShortRequestCard>
          <ShortRequestCard date="Заявка от 23.04.2024 в 12:50"
                            adress="Ул. Окская, д. 20"
                            info="Переполнены мусорные баки"
                            class="">
          </ShortRequestCard>
          <ShortRequestCard date="Заявка от 23.04.2024 в 12:50"
                            adress="Ул. Окская, д. 20"
                            info="Переполнены мусорные баки"
                            class="">
          </ShortRequestCard>
          <ShortRequestCard date="Заявка от 23.04.2024 в 12:50"
                            adress="Ул. Окская, д. 20"
                            info="Переполнены мусорные баки"
                            class="">
          </ShortRequestCard>
        </div>
      </div>
      <div class="request-card">
        <h4>Информация о заявке № 84</h4>
        <div class="request-card-content">
          <div class="request-card-up">
            <div class="request-card-info-block custom-scroll">
              <span>
                <b>Сообщение жителя:</b><br>
                Разбитое стекло в 3 подьезде
              </span>
              <span><b>Дата:</b> 23.04.2024 в 14:20</span>
              <span><b>Статус:</b> Новая</span>
              <span><b>Житель:</b> Беляков Леонид</span>
              <span><b>Адрес:</b> Ул. Волжская, д. 74</span>
            </div>
            <div class="request-card-photo-block">
              <span>
                <b>Прикреплённая фотография:</b><br>
                Житель не прикрепил фотографию
              </span>
            </div>
          </div>
          <div class="request-card-tasks-block">789</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import ShortRequestCard from "@/components/ShortRequestCard.vue";

export default {
  components: {ShortRequestCard, MyButton}
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  min-height: 400px;
  height: 94vh;
}

.left-side-menu {
  background-color: rgb(169, 168, 159, 0.2);
  width: 20%;
  padding: 10px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.logo-block {
  text-align: center;
}

.logo-img {
  width: 50%;
}

.menu-button {
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  padding-left: 20px;
  align-items: center;
}

.menu-button:hover {
  display: flex;
  background-color: rgb(109, 197, 195, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  padding-left: 20px;
  align-items: center;
  cursor: default;
}

.down-block {
  width: 100%;
}

.workspace {
  background-color: rgb(169, 168, 159, 0.2);
  width: 79%;
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-radius: 20px;
}

.requests-list {
  width: 35%;
  border: 1px;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px 10px 15px;
}

.requests-list-scroll {
  height: 95%;
  overflow-y: auto;
  padding-right: 3px;
  border-radius: 12px;
  //border: 1px solid black;
}

.request-card {
  width: 64%;
  //border: 1px solid #212523;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px;

}

.request-card-content {
  //border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 94%;
}

.request-card-up {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 49%;
  //border: 1px solid red;
  //padding: 10px;
}

.request-card-info-block {
  width: 49%;
  display: flex;
  flex-direction: column;
  //border: 1px solid yellow;
  overflow-y: auto;
}

.request-card-photo-block {
  width: 49%;
  //border: 1px solid pink;
}

.request-card-tasks-block {
  //border: 1px solid blue;
  height: 49%;
}

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}

.exit-button {
  width: 100%;
  border-radius: 20px;
  height: 40px;
}

.custom-scroll::-webkit-scrollbar {
  width: 5px; /* Ширина полосы прокрутки */
}

/* Фон полосы прокрутки */
.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
}

/* Стиль ползунка */
.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}

/* Цвет ползунка при наведении */
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>