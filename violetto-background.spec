# Violetto theme background
%define oname Violetto
%define bdate   2022.02.14

Summary:	Violetto theme background
Name:		violetto-background
Version:	1.0
Release:	5
License:	GPL
Group:		Graphics
Url:		https://github.com/rugyada/violetto-background
Source0:	%{oname}.tar.gz
BuildArch:	noarch

%description
Violetto theme background

%files
%dir %{_datadir}/wallpapers/Violetto/
%{_datadir}/wallpapers/Violetto/*

%prep
%setup -qn %{oname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers/Violetto
cp * %{buildroot}%{_datadir}/wallpapers/Violetto/

