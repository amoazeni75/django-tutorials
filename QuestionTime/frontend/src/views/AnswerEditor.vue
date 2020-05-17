//for creating and update the questions
<template>
    <div class="container mt-2">
        <h1 class="mb-3">Edit Your Answer</h1>
        <form @submit.prevent="onSubmit">
            <textarea rows="3"
                      v-model="answerBody"
                      class="form-control"
            >
            </textarea>
            <br>
            <button
                    type="submit"
                    class="btn btn-success"
            >
                Publish Your Answer
            </button>
        </form>
        <p v-if="error" class="muted mt-2">{{error}}</p>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "AnswerEditor",
        props: {
            id: {
                type: Number,
                required: true
            },
            // previousAnswer: { //the first way,
            //     type: String,
            //     required: true
            // },
            // questionSlug: { //the first way,
            //     type: String,
            //     required: true
            // }
        },
        data() {
            return {
                questionSlug: null, //second way
                answerBody: null, //second way
                // answerBody: this.previousAnswer, //the first way, getting extra props via beforeRouter
                error: null
            }
        },
        methods: {
            onSubmit() {
                if (this.answerBody) {
                    let endpoint = `/api/answers/${this.id}/`;
                    apiService(endpoint, "PUT", {body: this.answerBody})
                        .then(() => {
                            this.$router.push({
                                name: "Question",
                                params: {slug: this.questionSlug}
                            })
                        })
                } else {
                    this.error = "You can't submit an empty answer!"
                }
            }
        },
        async beforeRouteEnter(to, from, next) {
            let endpoint = `/api/answers/${to.params.id}/`
            let data = await apiService(endpoint)
            // to.params.previousAnswer = data.body; //first way
            // to.params.questionSlug = data.question_slug;
            // return next();

            return next(vm => {   // vm is like this, that refer to the current vue instance
                vm.questionSlug = data.question_slug;
                vm.answerBody = data.body
            })

        }
    }
</script>

<style scoped>

</style>