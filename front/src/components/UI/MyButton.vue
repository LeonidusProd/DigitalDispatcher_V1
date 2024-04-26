<template>
  <button class="my-btn my-btn-primary">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'my-button',
  props: {
    modelValue: [String, Number]
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style scoped>
.my-btn {
  margin-top: 5px;
  text-decoration: none;
  --bs-btn-padding-x: 0.75rem;
  --bs-btn-padding-y: 0.375rem;
  display: inline-block;
  padding: var(--bs-btn-padding-y) var(--bs-btn-padding-x);
  font-size: 1rem;
  color: #212523;
  background-color: #4fd4d5;
  text-align: center;
  vertical-align: middle;
  border: var(--bs-btn-border-width) solid var(--bs-btn-border-color);
  border-radius: 7px;
}

.my-btn:focus {
  background-color: #6dc5c3;
  border-color: #122b40
}
</style>