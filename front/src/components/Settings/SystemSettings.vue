<template>
  <div class="inside-container">
    <div class="left-side">
      <h3>Токен бота приёма заявок</h3>
      <my-input class="bot-token-input"
                :placeholder="'Вставьте токен бота'"
                :model-value="resBotToken"
                @input="this.resBotToken = $event.target.value">
      </my-input>

      <h3>Токен бота распределения задач</h3>
      <my-input class="bot-token-input"
                :placeholder="'Вставьте токен бота'"
                :model-value="staffBotToken"
                @input="this.staffBotToken = $event.target.value">
      </my-input>
    </div>

    <div class="right-side">
      <my-button @click="saveSettings"
                 class="save-button">
        Сохранить
      </my-button>
    </div>
  </div>
</template>

<script>

import {defineComponent} from "vue";
import MyInput from "@/components/UI/MyInput.vue";
import MySelect from "@/components/UI/MySelect.vue";
import MyButton from "@/components/UI/MyButton.vue";
import axios from "axios";

export default defineComponent({
  components: {MyButton, MySelect, MyInput},
  data() {
    return {
      resBotToken: 0,
      staffBotToken: 0
    }
  },
  mounted() {
    this.loadSettings()
  },
  methods: {
    async saveSettings() {
      try {
        const response = (
            await axios.put(
                'http://localhost:8000/api/v1/bottokens/manage/1',
                {
                  residentBotToken: this.resBotToken,
                  staffBotToken: this.staffBotToken
                }
            )
        )
      } catch (e) {
        alert('Сервер не доступен')
      }

    },
    async loadSettings() {
      try {
        const response = (await axios.get('http://localhost:8000/api/v1/bottokens/manage/1'))
        this.resBotToken = response.data.residentBotToken
        this.staffBotToken = response.data.staffBotToken
      } catch (e) {
        alert('Сервер не доступен')
      }

    }
  }
})
</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  //border: 1px solid black;
  height: 100%;
  width: 100%;
}

.left-side {
  width: 48%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  //border: 1px solid blue;
}

.right-side {
  width: 48%;
  display: flex;
  flex-direction: column;
  justify-content: end;
  align-items: end;
  //border: 1px solid red;
}

.bot-token-input {
  margin-bottom: 10px;
  //width: 400px;
  height: 40px;
}

.save-button {
  width: 200px;
}
</style>