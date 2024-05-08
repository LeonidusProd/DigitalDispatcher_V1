<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление отдела</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="closeDialog">
          </div>
        </div>

        <div class="down-block">
          <h5>Название отдела</h5>
          <MyInput :placeholder="'Название отдела'"
                   :model-value="this.departmentName"
                   @input="this.departmentName = $event.target.value">
          </MyInput>

          <MyButton @click="saveDepartment">
            Сохранить
          </MyButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MyInput from "@/components/UI/MyInput.vue";

export default {
  components: {MyButton, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      departmentName: '',
    }
  },
  methods: {
    closeDialog() {
      this.$emit('closeDepartmentDialog')
    },
    saveDepartment() {
      if (this.departmentName !== '') {
        this.$emit('saveDepartment', {
          name: this.departmentName,
        })
        this.departmentName = ''
      }
    },
  }
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgb(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
  z-index: 1000;
}
.dialog-content {
  margin: auto;
  background: white;
  border-radius: 12px;
  min-height: 220px;
  width: 400px;
  padding: 20px;
  display: flex;
}
.create-task-content {
  width: 100%;
  background: rgb(169, 168, 159, 0.2);
  border-radius: 10px;
  padding: 10px;
}
.up-block {
  height: 30px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
}
.down-block {
  height: 90%;
  width: 100%;
  padding: 20px;
}
.close-dialog-button {
  height: 30px;
  width: 30px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}
.close-dialog-button:hover {
  height: 30px;
  width: 30px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}
.close-dialog-button-img {
  width: 100%;
}
</style>