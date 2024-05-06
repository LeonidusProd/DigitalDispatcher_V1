<template>
  <div class="container">
    <div class="center-container">
      <div class="logo-box">
        <img class="logo-img" alt="logo"
             src="@/assets/Лого%20текст%20снизу.svg">
      </div>

      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Вход в систему</h5>

          <form>
            <div class="form-group">
              <label for="username">Имя пользователя</label>
              <!--            <input type="text" class="form-control" id="username" placeholder="Имя пользователя">-->
              <my-input type="text" id="username" placeholder="Имя пользователя"></my-input>
            </div>

            <div class="form-group">
              <label for="password">Пароль</label>
              <my-input type="password" id="password" placeholder="Пароль"></my-input>
              <!--            <input type="password" class="form-control" id="password" placeholder="Пароль">-->
            </div>

            <!--          <button type="submit" class="btn btn-primary">Войти</button>-->
            <my-button @click="">
              Войти
            </my-button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";

export default {
  components: {
    MyButton,
    MyInput
  },
}
</script>

<style scoped>
.card {
  border: 2px solid #a9a89f;
}

.center-container {
  display: flex;
  justify-content: center;
  flex-direction: row;
  align-items: center;
  gap: 100px; /*расстояние между иконкой и инпутом*/
  width: 1200px;
  height: 80vh;
}

.logo-img {
  height: 300px;
}
</style>