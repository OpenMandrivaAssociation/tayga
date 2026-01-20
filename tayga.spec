%global debug_package %{nil}

Name:		tayga
Version:	0.9.6
Release:	1
Source0:	https://github.com/apalrd/tayga/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Simple, no-fuss NAT64 for Linux 
URL:		https://github.com/apalrd/tayga
License:	GPL-2.0
Group:		Network

BuildRequires:	make

Requires:python-pyroute2

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux and FreeBSD. It uses the TUN driver to exchange packets with the kernel, which is the same driver used by OpenVPN and QEMU/KVM.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%license LICENSE
%{_prefix}/local/share/man/man5/*
%{_prefix}/local/share/man/man8/*
%{_prefix}/local/sbin/%{name}
