<template>
    <div class="not-found">
        <div class="container mt-3">
            <h1 id="notfound"> {{message}}</h1>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PageNotFound",
        props: {
            message: {
                type: String,
                default: "Page Not Found..."
            }
        }
    }
</script>

<style scoped>
    #notfound {
        color: red;
        text-align: center;
    }
</style>