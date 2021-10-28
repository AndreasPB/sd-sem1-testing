<script>
	import Footer from '../components/footer.svelte';
	import Navbar from '../components/navbar.svelte';

</script>

<body class="flex flex-col h-screen justify-between">
	<Navbar />
	<main class="flex-grow">
		<div class="container mx-auto">
            <!-- Main phone card -->
            <div class="mt-5 card bordered">
                <div class="card-body">
                    <h2 class="card-title">KEANet</h2>
                    <!-- Internet connection -->
                    <div class="p-6 card bordered">
                        <div class="form-control">
                            <label class="cursor-pointer label">
                                <span class="label-text">Internet connection</span>
                                <input type="checkbox" checked={false} class="checkbox checkbox-primary">
                            </label>
                        </div>
                    </div>
                    <!-- Phone line -->
                    <!-- Cell phones -->
                    <!-- Total price -->
                    <!-- Buy button -->
                </div>
            </div>
		</div>
	</main>
	<Footer />
</body>
