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
              <MyInput type="text"
                       id="username"
                       :placeholder="'Имя пользователя'"
                       :model-value="this.login"
                       @input="this.login = $event.target.value">
              </MyInput>
            </div>

            <div class="form-group">
              <label for="password">Пароль</label>
              <MyInput type="password"
                       id="password"
                       :placeholder="'Пароль'"
                       :model-value="this.password"
                       @input="this.password = $event.target.value">
              </MyInput>
            </div>

            <MyButton @click="getToken">
              Войти
            </MyButton>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import axios from "axios";

export default {
  components: {
    MyButton,
    MyInput
  },
  data() {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    async getToken() {
      try {
        const response = (await axios.post(
            `http://localhost:8000/auth/token/login`,
            {
              username: this.login,
              password: this.password
            }
        ))
        // this.offices = response.data
        // console.log(response.data)
        localStorage.setItem('auth_token', response.data.auth_token);
        localStorage.setItem('user_role', response.data.role);
        // console.log(localStorage.getItem('auth_token'))
        // console.log(localStorage.getItem('user_role'))
        if (localStorage.getItem('user_role') === 'staff') {
          this.$router.push('/requests');
        } else if (localStorage.getItem('user_role') === 'admin') {
          this.$router.push('/settings');
        } else {
          alert('У вас нет прав доступа')
        }
      } catch (e) {
        alert('Сервер не доступен')
        console.log(e)
      }
    },
  }
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