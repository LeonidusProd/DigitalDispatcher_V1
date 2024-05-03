<template>
  <div class="request-short-card">
    <span>Заявка от {{ date.split(' ')[0] }} в {{ date.split(' ')[1] }}</span>
    <span>{{ adress }}</span>
    <div class="request-short-text">
      {{ info }}
    </div>
  </div>
</template>

<script>
export default {
  props: ['date', 'adress', 'info'],
}
</script>

<style scoped>
.request-short-card {
  background-color: rgb(139, 182, 177, 0.4);
  display: flex;
  flex-direction: column;
  //border: 1px solid ;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
}

.request-short-card:hover {
  background-color: rgb(109, 197, 195, 0.4);
  display: flex;
  flex-direction: column;
  cursor: default;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
}

.request-short-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>