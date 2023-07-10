<template>
    <div>
        <input type="text">
    </div>
</template>

<style>
input {
    border-radius: 20px;
}
</style>

<script>
fetch('https://google.com/')
.then((x) => x.text())
.then((x) => console.log(x));
</script>