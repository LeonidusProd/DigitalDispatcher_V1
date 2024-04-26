<template>
  <div class="center-container">
    <div class="logo-box">
      <img class="logo-img" alt="logo"
           src="http://localhost:8000/media/assets/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D1%81%D0%BD%D0%B8%D0%B7%D1%83.png">
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
          <my-button>Войти</my-button>
        </form>
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
.card{
  border: 2px solid #a9a89f;
}

.center-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 100vh;
}

.logo-img {
  height: 300px;
}
</style>