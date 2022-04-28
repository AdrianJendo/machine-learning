import { useState } from "react";
import Link from "next/link";
import Head from "next/head";
import Image from "next/image";

export default function HomePage() {
	return (
		<>
			<Head>
				<title>Create Next App</title>
				<link rel="icon" href="/favicon.ico" />
			</Head>
			<main>
				<h1 className="title">
					Read{" "}
					<Link href="/algorithms/cat-vs-dog">
						<a>this page!</a>
					</Link>
					<Image
						src="/images/logo.png" // Route of the image file
						height={72} // Desired size with correct aspect ratio
						width={144} // Desired size with correct aspect ratio
						alt="Your Name"
					/>
				</h1>
			</main>
		</>
	);
}
