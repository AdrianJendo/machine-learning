import React, { useState } from "react";

// mui
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { styled } from "@mui/material/styles";
import { Box, AppBar, Toolbar, Typography } from "@mui/material";

import Link from "next/link";
import Head from "next/head";
import Image from "next/image";

import { theme } from "src/theme/theme";

const Main = styled("div")(
    ({ theme }) => `
		background-color: ${theme.palette.background.default};
		width: 100%;
		height: calc(100vh - 64px);
	`
);

export default function HomePage() {
    return <div>Hello World</div>;
}
