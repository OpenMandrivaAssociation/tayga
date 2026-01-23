#some of the prep and install parts were taken from the Fedora spec file for tayga
%undefine _debugsource_template

Name:		tayga
Version:	0.9.6
Release:	2
Source0:	https://github.com/apalrd/tayga/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:  tayga.tmpfilesd.conf
Summary:	Simple, no-fuss NAT64 for Linux 
URL:		https://github.com/apalrd/tayga
License:	GPL-2.0
Group:		Network

BuildRequires:	make
BuildRequires:  coreutils
BuildRequires:  pkgconfig(libnl-3.0)

Requires:  python-pyroute2
Requires:  iproute2

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux and FreeBSD. It uses the TUN driver to exchange packets with the kernel, which is the same driver used by OpenVPN and QEMU/KVM.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install prefix=%{_prefix} sbindir=%{_sbindir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -p -D -m 0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/%{name}.conf

sed -i 's,%i,default,g' scripts/%{name}@.service
install -p -D -m 0644 scripts/%{name}@.service %{buildroot}/%{_unitdir}/%{name}.service

install -D -m 0644 /dev/stdin %{buildroot}%{_sysconfdir}/%{name}.conf <<'EOF'
tun-device nat64
ipv4-addr 192.168.255.1
prefix 2001:db8:1:ffff::/96
dynamic-pool 192.168.255.0/24
data-dir /var/db/tayga
EOF

%post
%tmpfiles_create_package %{name} %{name}.tmpfilesd.conf
%systemd_post %{name}

%preun
%systemd_preun %{name}@.service

%files
%license LICENSE
%config(noreplace) /etc/%{name}.conf
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
