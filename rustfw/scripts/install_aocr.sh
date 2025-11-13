#!/bin/bash
# Setup script to install aocr CLI globally

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🦀 Installing aocr (Advent of Code Rust CLI)${NC}"
echo ""

# Find the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUSTFW_DIR="${PROJECT_ROOT}/rustfw"
AOCR_BINARY="${RUSTFW_DIR}/target/release/aocr"

echo "Project root: ${PROJECT_ROOT}"
echo "Rustfw dir: ${RUSTFW_DIR}"

# Check if binary exists
if [ ! -f "${AOCR_BINARY}" ]; then
    echo -e "${BLUE}Building aocr binary...${NC}"
    cd "${RUSTFW_DIR}"
    cargo build --bin aocr --release
    cd - > /dev/null
fi

if [ ! -f "${AOCR_BINARY}" ]; then
    echo -e "${RED}❌ Failed to build aocr binary${NC}"
    exit 1
fi

echo -e "${GREEN}✅ aocr binary built successfully${NC}"
echo ""

# Create symlink in /usr/local/bin
echo -e "${BLUE}Creating symlink in /usr/local/bin...${NC}"

# Check if we need sudo
if [ -w /usr/local/bin ]; then
    ln -sf "${AOCR_BINARY}" /usr/local/bin/aocr
else
    sudo ln -sf "${AOCR_BINARY}" /usr/local/bin/aocr
fi

chmod +x /usr/local/bin/aocr

echo -e "${GREEN}✅ Symlink created${NC}"
echo ""

# Verify installation
echo -e "${BLUE}Verifying installation...${NC}"
which aocr

echo ""
echo -e "${GREEN}✅ Installation complete!${NC}"
echo ""
echo "You can now use aocr from anywhere:"
echo "  aocr 2024 1              # Run day 1"
echo "  aocr 2024 --days 1-5     # Run days 1-5"
echo "  aocr 2024 --days 1,3,5   # Run specific days"
echo ""
