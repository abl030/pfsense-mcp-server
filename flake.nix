{
  description = "pfSense MCP Server development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python312;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          (python.withPackages (ps: with ps; [
            httpx
            python-dotenv
            pytest
            pytest-asyncio
          ]))
        ];

        shellHook = ''
          if [ -f /run/secrets/mcp/pfsense.env ]; then
            set -a
            source /run/secrets/mcp/pfsense.env
            set +a
            export PFSENSE_URL="$PFSENSE_HOST"
          fi
        '';
      };
    };
}
