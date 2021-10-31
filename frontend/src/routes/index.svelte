<script>
  import { onMount } from 'svelte';
	import Footer from '../components/footer.svelte';
	import Navbar from '../components/navbar.svelte';

  let phones = [];
	let purchaseTotal = 0;
	let phoneLines = 0;
	let selectedPhones = [];
	let internetConnection = false;

	const updateAmount = async (name, amount) => {
		for (let i = 0; i < selectedPhones.length; i++) {
			if (selectedPhones[i].name === name) {
				selectedPhones[i].amount = amount;
			}
		}
	};

	const buildShoppingCartPayload = async () => {
		let shoppingCart = {
			internet_connection: undefined,
			phone_lines: undefined,
			cell_phones: undefined
		};

		if (internetConnection) {
			shoppingCart.internet_connection = {
				price: 200,
				regularity: 'Monthly'
			};
		}
		if (phoneLines) {
			shoppingCart.phone_lines = {
				price: 150,
				amount: phoneLines,
				regularity: 'Monthly'
			};
		}
		if (selectedPhones) {
			shoppingCart.cell_phones = selectedPhones;
		}
		return shoppingCart;
	};

	const fetchCellPhones = async () => {
		return fetch('http://localhost:2000/cellphones')
			.then((response) => response.json())
			.then((data) => data)
	};

	const fetchRunningTotal = async () => {
		const payload = await buildShoppingCartPayload();
		fetch('http://localhost:2000/totalprice', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(payload)
		})
			.then((response) => response.json())
			.then((data) => (purchaseTotal = data.total_price));
	};

  onMount(async () => {
    phones = await fetchCellPhones();
  })

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
					<div class="p-3 card bordered">
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text">Internet connection</span>
								<input
									type="checkbox"
									bind:checked={internetConnection}
									on:change={fetchRunningTotal}
									class="checkbox checkbox-primary"
								/>
							</label>
						</div>
					</div>
					<!-- Phone line -->
					<p class="pt-4">Phone lines: {phoneLines}</p>
					<input
						type="range"
						max="8"
						bind:value={phoneLines}
						on:change={fetchRunningTotal}
						class="range range-primary"
					/>
					<!-- Cell phones -->
					<div class="overflow-x-auto pt-4">
							<table class="table w-full table-compact">
								<thead>
									<tr>
										<th>Name</th>
										<th>Price</th>
										<th>Amount</th>
										<th>Regularity</th>
										<th>Purchase?</th>
									</tr>
								</thead>
								<tbody>
									{#each phones as phone}
										<tr>
											<td>
												{phone.name}
											</td>
											<td>
												{phone.price * phone.amount}
											</td>
											<td>
												<select
													class="select"
													bind:value={phone.amount}
													on:change={updateAmount(phone.name, phone.amount)}
													on:change={fetchRunningTotal}
												>
													<option disabled>Amount</option>
													{#each Array(10) as _, i}
														<option>{i + 1}</option>
													{/each}
												</select>
											</td>
											<td>
												{phone.regularity}
											</td>
											<td>
												<div class="form-control">
													<label class="cursor-pointer label">
														<input
															type="checkbox"
															checked={false}
															class="checkbox checkbox-primary"
															value={phone}
															bind:group={selectedPhones}
															on:change={fetchRunningTotal}
														/>
													</label>
												</div>
											</td>
										</tr>
									{/each}
								</tbody>
							</table>
					</div>
					<!-- Total price -->
					<div class="card text-center pt-4">
						<h2>Total price: {purchaseTotal} DKK</h2>
					</div>
				</div>
				<!-- Buy button -->
				<button class="btn btn-primary">Buy</button>
			</div>
		</div>
	</main>
	<Footer />
</body>
