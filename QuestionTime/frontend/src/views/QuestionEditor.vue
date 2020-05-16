//for creating and update the questions
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Ask a Question</h1>
        <form @submit.prevent="onSubmit">
            <textarea rows="3"
                      v-model="question_body"
                      class="form-control"
                      placeholder="what do you want to ask?"
            >
            </textarea>
            <br>
            <button
                    type="submit"
                    class="btn btn-success"
            >
                Publish
            </button>
        </form>
        <p v-if="error" class="muted mt-2">{{error}}</p>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "QuestionEditor",
        data() {
            return {
                question_body: null,
                error: null
            }
        },
        methods: {
            onSubmit() {
                if (!this.question_body) {
                    this.error = "You cant't send empty question!"
                } else if (this.question_body.length > 240) {
                    this.error = "Nor more than 240 characters"
                } else {
                    let endpoint = "/api/questions/"
                    let method = "POST"
                    apiService(endpoint, method, {content: this.question_body})
                        .then(value => {
                            this.$router.push(
                                {
                                    name: "Question",
                                    params: {slug: value.slug}
                                }
                            )
                        })
                }
            }
        },
        created() {
            document.title = "Editor - QuestionTime"
        }
    }
</script>

<style scoped>

</style>