%define oname violetto-background

Summary:    Violetto background
Name:   violetto-background
Version:    1
Release:    1
License:    GPL
Group:  Graphical desktop/KDE
Url:    https://github.com/rugyada/violetto-background
Source0:    violetto-background.tar.gz

BuildRequires:	extra-cmake-modules
BuildArch:	noarch

%description
Violetto background

%files
%dir %{_datadir}/wallpapers/Violetto/
%{_datadir}/wallpapers/Violetto/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers/Violetto
cp * %{buildroot}%{_datadir}/wallpapers/Violetto
