// index.html
import { useState } from "react";
import Link from "next/link";

export default function HomePage() {
	return (
		<h1 className="title">
			Read{" "}
			<Link href="/algorithms/cat-vs-dog">
				<a>this page!</a>
			</Link>
		</h1>
	);
}
